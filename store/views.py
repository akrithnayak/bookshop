from django.shortcuts import render, redirect
import ast, sys, os
from django.http import HttpResponse


# books = [
#     {
#         "author": "Leo Tolstoy",
#         "name": "Anna Kareninan",
#         "desc": "Any fan of stories that involve juicy subjects like adultery, gambling, marriage plots, and, well, Russian feudalism, would instantly place Anna Karenina at the peak of their “greatest novels” list. And that’s exactly the ranking that publications like Time magazine have given the novel since it was published in its entirety in 1878. Written by Russian novelist Leo Tolstoy, the eight-part towering work of fiction tells the story of two major characters: a tragic, disenchanted housewife, the titular Anna, who runs off with her young lover, and a lovestruck landowner named Konstantin Levin, who struggles in faith and philosophy. Tolstoy molds together thoughtful discussions on love, pain, and family in Russian society with a sizable cast of characters regarded for their realistic humanity. The novel was especially revolutionary in its treatment of women, depicting prejudices and social hardships of the time with vivid emotion.",
#         "date": "1877",
#         "quan": "40"
#     },
#     {
#         "author": "Harper Lee",
#         "name": "To Kill a Mockingbirdman",
#         "date": "1960",
#         "quan": "30",
#         "desc": "Harper Lee, believed to be one of the most influential authors to have ever existed, famously published only a single novel (up until its controversial sequel was published in 2015 just before her death). Lee’s To Kill a Mockingbird was published in 1960 and became an immediate classic of literature. The novel examines racism in the American South through the innocent wide eyes of a clever young girl named Jean Louise (“Scout”) Finch. Its iconic characters, most notably the sympathetic and just lawyer and father Atticus Finch, served as role models and changed perspectives in the United States at a time when tensions regarding race were high. To Kill a Mockingbird earned the Pulitzer Prize for fiction in 1961 and was made into an Academy Award-winning film in 1962, giving the story and its characters further life and influence over the American social sphere."
#     },
#     {
#         "author": "F. Scott Fitzgerald",
#         "name": "The Great Gatsby",
#         "date": "10 April 1925",
#         "quan": "35",
#         "desc": "F. Scott Fitzgerald’s The Great Gatsby is distinguished as one of the greatest texts for introducing students to the art of reading literature critically (which means you may have read it in school). The novel is told from the perspective of a young man named Nick Carraway who has recently moved to New York City and is befriended by his eccentric nouveau riche neighbor with mysterious origins, Jay Gatsby. The Great Gatsby provides an insider’s look into the Jazz Age of the 1920s in United States history while at the same time critiquing the idea of the “American Dream.” Perhaps the most-famous aspect of the novel is its cover art—a piercing face projected onto a dark blue night sky and lights from a cityscape—an image that is also found, in a slightly different configuration, within the text itself as a key symbol."
#     },
#     {
#         "author": "Gabriel García Márquez",
#         "name": "One Hundred Years of Solitude",
#         "date": "1967",
#         "quan": "20",
#         "desc": "The late Colombian author Gabriel García Márquez published his most-famous work, One Hundred Years of Solitude, in 1967. The novel tells the story of seven generations of the Buendía family and follows the establishment of their town Macondo until its destruction along with the last of the family’s descendents. In fantastical form, the novel explores the genre of magic realism by emphasizing the extraordinary nature of commonplace things while mystical things are shown to be common. Márquez highlights the prevalence and power of myth and folktale in relating history and Latin American culture. The novel won many awards for Márquez, leading the way to his eventual honor of the Nobel Prize for Literature in 1982 for his entire body of work, of which One Hundred Years of Solitude is often lauded as his most triumphant."
#     },
#     {
#         "author": "E.M. Forster",
#         "name": "A Passage to India",
#         "date": "1924",
#         "quan": "30",
#         "desc": "E.M. Forster wrote his novel A Passage to India after multiple trips to the country throughout his early life. The book was published in 1924 and follows a Muslim Indian doctor named Aziz and his relationships with an English professor, Cyril Fielding, and a visiting English schoolteacher named Adela Quested. When Adela believes that Aziz has assaulted her while on a trip to the Marabar caves near the fictional city of Chandrapore, where the story is set, tensions between the Indian community and the colonial British community rise. The possibility of friendship and connection between English and Indian people, despite their cultural differences and imperial tensions, is explored in the conflict. The novel’s colorful descriptions of nature, the landscape of India, and the figurative power that they are given within the text solidifies it as a great work of fiction."
#     }
# ]




def result(request):

    if request.GET.get('book'):
        res = searchBook(request.GET.get('book'))
        return render(request, "store/result.html", res)
    else:
        return redirect("/")

def searchBook(search):
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r")
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
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r")
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
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r")
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
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r")
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
    file = open(os.path.join(sys.path[0], "store/books.txt"), "r")
    books = ast.literal_eval(file.read())
    file.close()
    new = {"name": name, "author": author, "date": date, "quan": quan, "desc": desc}
    books[index] = new
    file = open(os.path.join(sys.path[0], "store/books.txt"), "w")
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
        file = open(os.path.join(sys.path[0], "store/books.txt"), "r")
        books = ast.literal_eval(file.read())
        file.close()
        new = {"name": name, "author": author, "date": date, "quan": quan, "desc": desc}
        books.append(new)
        file = open(os.path.join(sys.path[0], "store/books.txt"), "w")
        file.write(str(books))
        file.close()
        return redirect("/admin/home")
    return render(request, "store/admin_add.html", {"title": "Admin"})
    
def adminDelete(request):
    if request.GET.get("book"):
        res = searchBookForEdit(request.GET.get("book"))
        if(res["flag"]):
            file = open(os.path.join(sys.path[0], "store/books.txt"), "r")
            books = ast.literal_eval(file.read())
            file.close()
            books.remove(res['book'])
            file = open(os.path.join(sys.path[0], "store/books.txt"), "w")
            file.write(str(books))
            file.close()
            return render(request, "store/admin_delete.html", {"title": "Admin", "true": True})
        return render(request, "store/admin_delete.html", {"title": "Admin", "false": True})
    return render(request, "store/admin_delete.html", {"title": "Admin"})
    

