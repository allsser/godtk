import hashlib
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from .models import Hashtag
from .models import Godtk
from .forms import GodtkForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.db.models import Q

def index(request):
    godtk = Godtk.objects.all()[::-1]
    context = {'godtk' : godtk}
    return render(request, 'godtk/index.html', context)

def detail(request, godtk_pk):
    godtk = get_object_or_404(Godtk, pk=godtk_pk)

    context = {
        'godtk': godtk,
    }
    return render(request, 'godtk/detail.html', context)

def hashtag(request, hash_pk):
  # 해시태그 가져오기
  hashtag = get_object_or_404(Hashtag, pk=hash_pk)
  # 해당 해시태그를 참조하는 게시글들 가져오기
  godtk = hashtag.godtk_set.order_by('-pk')
  context = {
    'hashtag' : hashtag,
    'godtk' : godtk,
  }
  return render(request, 'godtk/hashtag.html', context)

def search(request):
    # 사용자가 입력한 검색어 가져오기
    query = request.GET.get('query')
    # DB에서 query가 포함된 제목을 가진 artice 가져오기 (LIKE)
    # __contatins : 지정한 문자열 포함하는 자료검색
    # __icontains : 지정한 문자열 포함하는 자료검색(대소문자 구별 X)
    godtk = Godtk.objects.filter(event_title__icontains=query)

    # context로 전달
    context = {'godtk': godtk}
    return render(request, 'godtk/search.html',context)

def create(request):
    if request.user.is_authenticated: #작성자가 같은경우만
        if request.method == 'POST':
            # Binding 과정
            # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다.
            # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다. (그래서 변수에 담음)
            form = GodtkForm(request.POST, request.FILES)
            # embed()
            if form.is_valid():
                godtk = form.save(commit=False)
                godtk.user = request.user
                godtk.save()

                # hashtag
                # 게시글 내용을 split해서 리스트로 만듦
                for word in godtk.tag.split():
                    # word가 '#'으로 시작할 경우 해시태그 등록
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(tag=word)
                        godtk.hashtag.add(hashtag)


            return redirect('godtk:detail', godtk.pk)
        else:
            form = GodtkForm()

        # form으로 전달받는 형태가 2가지
        # 1. GET 요청 -> 비어있는 폼 전달
        # 2. 유효성 검증 실패 -> 에러 메세지를 포함한 채로 폼 전달
        context = {'form':form}
        return render(request,'godtk/form.html', context)
    else:
        return redirect('godtk:index')

def update(request, godtk_pk):
    godtk = get_object_or_404(Godtk, pk=godtk_pk)
    if request.user.is_authenticated: #작성자가 같은경우만
        if request.method == "POST":
            form = GodtkForm(request.POST, request.FILES, instance=godtk)
            if form.is_valid():
                godtk = form.save()
                # hashtag
                godtk.hashtag.clear()
                for word in godtk.content.split():
                    if word.startswith('#'):
                        hashtag, create = Hashtag.objects.get_or_create(content=word)
                        godtk.hashtag.add(hashtag)
                return redirect('godtk:detail', godtk.pk)
        else:
            form = GodtkForm(instance=godtk)       
    else:
        return redirect('godtk/index')   

    # context로 전달되는 2가지 form 형식
    # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
    # 2. POST -> is_valid가 False가 리턴됬을 때, 오류 메세지를 포함해서 동작한다.
    context = {
        'form':form,
        'godtk':godtk
    }
    return render(request, 'godtk/form.html', context)

@require_POST
def delete(request, godtk_pk):    
    if request.user.is_authenticated:#사용자가 로그인 되어 있는지
        godtk = get_object_or_404(Godtk,pk=godtk_pk) #삭제할 게시글
        godtk.delete()

    return redirect('godtk:index')