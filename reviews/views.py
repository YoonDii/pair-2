from django.shortcuts import redirect, render
from django.db.models import Q
from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


def index(request):
    reviews = Review.objects.order_by("-id")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:search")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/form.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/form.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)

    review.delete()

    return redirect("reviews:index")


def search(request):
    all_data = Review.objects.all()
    search = request.GET.get("search", "")
    if search:
        search_list = all_data.filter(
            Q(title__icontains=search) | Q(movie_name__icontains=search)
        )

        context = {
            "search_list": search_list,
        }
    else:
        context = {
            "search_list": all_data,
        }

    return render(request, "reviews/search.html", context)
