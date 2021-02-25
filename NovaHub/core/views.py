from django.shortcuts import render
from upload.forms import FileForm
from django.shortcuts import redirect
from upload.models import File
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from upload.services import get_file_size


# view to handle file uploads
@login_required
def upload(request):

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if request.is_ajax():
            if form.is_valid():
                form.save(request.user)
                # upload_task = process_up_load(form).delay(10)
                print("Successfully uploaded file: ", request.FILES['uploaded_file'].name)

                context = {"form": form}
                # return render(request, "upload.html", context)
                return redirect('core:index')
            else:
                return render(request, "upload.html", {'form': form})
    else:
        form = FileForm()
        return render(request, "upload.html", {'form': form})


# Function to add all sizes
# and return total size
def add_all(file_list):
    total = 0
    for file in file_list:
        total = total + file.get_size
    return total


# view for the index page
# retrieves all current logged in user files
@login_required
def index(request):
    files = File.objects.filter(Q(user=request.user))

    # call add_all function
    # and assign to total
    total = add_all(files)

    # call function to show size in MB
    # and assign to 'total_space'
    total_space_used = get_file_size(total)

    # set context for template
    context = {"files": files,
               "total_space_used": total_space_used,
               "count": files.count()}

    return render(request, "index.html", context)


# view to handle search feature
# retrieves files by matching name
@login_required
def search(request):
    query = request.GET.get('query')
    queryset = []
    exists = False

    if request.method == 'GET':
        if query:
            queryset = File.objects.filter(Q(uploaded_file__iexact=query) |
                                                  Q(uploaded_file__icontains=query))
            exists = queryset.exists()

    context = {'queryset': queryset, 'exists': exists, 'query': query}
    return render(request, 'search.html', context)


# view to delete a user file
def delete(request, id):
    file = get_object_or_404(File, id=id)
    if request.method == "POST":
        file.delete()
        return redirect('core:index')

    context = {"file": file}
    return render(request, "delete.html", context)


# view to delete all user files
def delete_all(request):
    files = File.objects.all()
    if request.method == "POST":
        files.delete()
        return redirect('core:index')

    context = {"files": files}
    return render(request, "delete.html", context)
