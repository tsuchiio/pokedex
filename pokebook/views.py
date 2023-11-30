from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView, ListView,CreateView,DetailView,FormView
from .models import Pokepost
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import PokepostForm,ContactForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView,UpdateView
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator,Page
from urllib.parse import urlencode

class IndexView(ListView):
    template_name = 'index.html'
    model=Pokepost
    context_object_name='pokemon_list'
    ordering=['-posted_at']
    paginate_by=9

class PokedexView(View):
    # model = Pokepost
    template_name = 'pokedex.html'
    # context_object_name = 'pokemon_list'
    paginate_by = 15
    
    def get(self, request, *args, **kwargs):
        age = request.session.get('age', 'all')
        type_filter = request.session.get('type', '')
        name_filter = request.session.get('name', '')
        order_by = request.session.get('order_by', 'num')
        sort_order = request.session.get('sort_order', '昇順')

        queryset = Pokepost.objects.all()

        # 世代のフィルター
        age = self.request.GET.get('age')
        if age and age   != 'all':
            queryset = queryset.filter(age=age)

        # タイプのフィルター
        type_filter = self.request.GET.get('type')
        if type_filter:
            queryset = queryset.filter(Q(type1=type_filter) | Q(type2=type_filter))

        # 名前の部分一致検索
        name_filter = self.request.GET.get('name')
        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)

        # ソートの指定
        order_by = self.request.GET.get('order_by',None)
        sort_order = self.request.GET.get('sort_order',None)
        if order_by == '-posted_at':
            if sort_order == '降順':
                queryset = queryset.order_by('posted_at')
            else:
                queryset = queryset.order_by('-posted_at')
        else:
            if sort_order == '降順':
                queryset = queryset.order_by('-num')
            else:
                queryset = queryset.order_by('num')
        
        paginator = Paginator(queryset,self.paginate_by)
        page = request.GET.get('page')
        paged_pokemon_list = paginator.get_page(page)
        pagination_params = request.GET.copy()
        if 'page' in pagination_params:
            del pagination_params['page']
        context = {
            'pokemon_list':paged_pokemon_list,
            'age':age,
            'type_filter':type_filter,
            'name_filter':name_filter,
            'order_by':order_by,
            'sort_order':sort_order,
            'pagination_params': pagination_params.urlencode(),
        }
        return render(request,self.template_name,context)
    
    def post(self,request,*args, **kwargs):
        request.session['age'] = request.POST.get('age', 'all')
        request.session['type'] = request.POST.get('type', '')
        request.session['name'] = request.POST.get('name', '')
        request.session['order_by'] = request.POST.get('order_by', 'num')
        request.session['sort_order'] = request.POST.get('sort_order', '昇順')
        return redirect('pokebook:pokedex')
    
    
@method_decorator(login_required, name='dispatch')
class PokepostView(CreateView):
    form_class=PokepostForm
    template_name = 'pokepost.html'
    success_url = reverse_lazy('pokebook:pokesuccess')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()  
        return super().form_valid(form)

class PokepostSuccess(TemplateView):
    template_name='pokepost_success.html'

class PokeDeleteView(DeleteView):
    model = Pokepost
    template_name = 'poke_delete.html'
    success_url = reverse_lazy('pokebook:index')
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model,pk=pk)

class PokeDetail(DetailView):
    template_name='pokedetail.html'
    model=Pokepost

class PokeUpdata(UpdateView):
    model = Pokepost
    form_class = PokepostForm
    template_name='pokeedit.html'
    def get_success_url(self) -> str:
        return reverse('pokebook:pokedetail', args=[str(self.object.id)])
    def form_valid(self,form):
        return super().form_valid(form)

class PokeMypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 15
    def get_queryset(self):
        queryset = Pokepost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return queryset

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pokebook:contact_success')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject =  'お問い合わせ：{}'.format(title)
        message = \
            '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}' \
            .format(name, email, title, message)
        from_email = 'tky2302050@stu.o-hara.ac.jp'
        to_list = ['tky2302050@stu.o-hara.ac.jp']
        message = EmailMessage(subject=subject,
                                                    body=message,
                                                    from_email=from_email,
                                                    to=to_list,
                                                    )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)

class ContactSuccess(TemplateView):
    template_name="contact_success.html"


class CustomPagenator(Paginator):
    def get_page(self, number):
        return CustomPage(self.object_list, number,self)

class CustomPage(Page):
    def get_full_path(self):
        params = self.paginator.data
        params['page'] = self.number
        return f"{self.paginator.base_url}?{urlencode(params)}"

