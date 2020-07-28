from django.shortcuts import render, redirect
import ast, sys, os
from django.http import HttpResponse





def result(request):

    if request.GET.get('book'):
        res = searchBook(request.GET.get('book'))
        return render(request, "store/result.html", res)
    else:
        return redirect("/")

def searchBook(search):
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r", encoding="utf-8")
    books = ast.literal_eval(file.read())
    file.close()
    if(search != ""):
        flag = False
        res = ""
        for book in books:
            if(book["name"].lower() == search.lower()):
                res = book
                flag = True
                break
        
        return {"flag": flag, "book": res}
    
        

def home(request):
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r", encoding="utf-8")
    books = ast.literal_eval(file.read())
    file.close()
    context = {
        "books": books[:5]
    }
    
    return render(request, "store/home.html", context)

def about(request):
    context = {
        "title": "About"
    }
    return render(request, "store/about.html", context)

def admin(request):
    return render(request, "store/admin.html", {"title": "Admin"})


def adminHome(request):
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r", encoding="utf-8")
    books = ast.literal_eval(file.read())
    file.close()
    context = {
        "books": books,
        "title": "Admin"
    }
    return render(request, "store/admin_home.html", context)


def adminAuth(request):
    u = ["ashwini", "akrith"]
    p = ["ashwini", "123"]
    uname = request.POST.get("uname")
    pswd = request.POST.get("pswd")
    if(uname in u):
        pas = u.index(uname)
        if(pswd == p[pas]):
            return redirect("/admin/home")
    return render(request, "store/wadmin.html")

def searchBookForEdit(search):
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r", encoding="utf-8")
    books = ast.literal_eval(file.read())
    file.close()
    if(search != ""):
        flag = False
        res = ""
        i = 0
        for book in books:
            if(book["name"].lower() == search.lower()):
                res = book
                flag = True
                break
            i+=1
       
        return {"flag": flag, "book": res, "index": i}
    

def adminSave(request):
    name = request.POST.get("name")
    author = request.POST.get("author", "")
    date = request.POST.get("date"," ")
    quan = request.POST.get("quan", "")
    desc = request.POST.get("desc"," ")
    index = int(request.POST.get("index"))
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r", encoding="utf-8")
    books = ast.literal_eval(file.read())
    file.close()
    new = {"name": name, "author": author, "date": date, "quan": quan, "desc": desc}
    books[index] = new
    file = open(os.path.join(sys.path[0], "store/books.txt"), "w", encoding="utf-8")
    file.write(str(books))
    file.close()
    return redirect("/admin/home")

def adminSearch(request):
    if request.GET.get('book'):
        res = searchBookForEdit(request.GET.get('book'))
        return render(request, "store/admin_home_edit.html", res)
    else:
        return redirect("/admin/home")

def adminAdd(request):
    if request.POST.get("name"):
        name = request.POST.get("name")
        author = request.POST.get("author", "")
        date = request.POST.get("date"," ")
        quan = request.POST.get("quan", "")
        desc = request.POST.get("desc"," ")
        file = open(os.path.join(sys.path[0], "store/books.txt"), "r", encoding="utf-8")
        books = ast.literal_eval(file.read())
        file.close()
        new = {"name": name, "author": author, "date": date, "quan": quan, "desc": desc}
        books.append(new)
        file = open(os.path.join(sys.path[0], "store/books.txt"), "w", encoding="utf-8")
        file.write(str(books))
        file.close()
        return redirect("/admin/home")
    return render(request, "store/admin_add.html", {"title": "Admin"})
    
def adminDelete(request):
    if request.GET.get("book"):
        res = searchBookForEdit(request.GET.get("book"))
        if(res["flag"]):
            file = open(os.path.join(sys.path[0], "store/books.txt"), "r", encoding="utf-8")
            books = ast.literal_eval(file.read())
            file.close()
            books.remove(res['book'])
            file = open(os.path.join(sys.path[0], "store/books.txt"), "w", encoding="utf-8")
            file.write(str(books))
            file.close()
            return render(request, "store/admin_delete.html", {"title": "Admin", "true": True})
        return render(request, "store/admin_delete.html", {"title": "Admin", "false": True})
    return render(request, "store/admin_delete.html", {"title": "Admin"})
    

