from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dict = {
    "january" : "eat no meat",
    "february" : "eat no chicken",
    "march" : "laugh a lot",
    "april" : "april's fool",
    "may" : "kings birthdays",
    "june" : "exams are gone",
    "july" : "take a break, take kitkat",
    "august" : "sweet holidays",
    "september" : "back to school",
    "october" : "winter time",
    "november" : "prepare for mid-year exams",
    "december" : None,   
    # "1" : "NUMBER eat no meat",
    # "2" : "NUMBER eat no chicken",
    # "3" : "NUMBER laugh a lot",
    # "4" : "NUMBER april's fool",
    # "5" : "NUMBER kings birthdays",
    # "6" : "NUMBER exams are gone",
    # "7" : "NUMBER take a break, take kitkat",
    # "8" : "NUMBER sweet holidays",
    # "9" : "NUMBER back to school",
    # "10" : "NUMBER winter time",
    # "11" : "NUMBER prepare for mid-year exams",
    # "12" : "NUMBER exam time"   
}
# Create your views here.
# def january(request):
#     return HttpResponse("This works!")

# def february(request):
#     return HttpResponse("february")

def index(request):
    months = list(monthly_challenges_dict.keys())
    return render(request, "challenges/index.html", {
        "months" : months
    })
    # list_items = ""
    # print(months)
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"    
    # response_data = f"""
    #     <ul>
    #         {list_items}           
    #     </ul>
    # """
    # return HttpResponse(response_data)

def monthly_challenge_by_numbers(request, month):
    months = list(monthly_challenges_dict.keys())
    
    if month > len(months) or month <= 0:
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/january
    # return HttpResponseRedirect(redirect_month)
    return HttpResponseRedirect(redirect_path)
    
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data) 
        return render(request,"challenges/challenge.html", {
            "month": month.capitalize(),
            "text": challenge_text
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()