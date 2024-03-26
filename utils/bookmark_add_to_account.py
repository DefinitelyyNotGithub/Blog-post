from Blog_Post.models import Post

def add_bookmarks_to_account(request):
    if 'saved' in request.session:
        for ID in request.session['saved']:
            post = Post.objects.get(id=ID)
            post.BookMarks.add(request.user)
            request.session['saved'].remove(ID)
            request.session.save()

