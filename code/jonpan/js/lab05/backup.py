def pokemon(request):
        search_term = request.GET.get("searchTerm")
        if search_term != None:
            pokemon = Pokemon.objects.filter(name__contains=f"{search_term}")
            data_to_return = pokemon.values("number", "name", "image_front")
            paginator = Paginator(data_to_return, 20)
            page_number = request.GET.get('page')
            data = list(paginator.get_page(page_number))
            return JsonResponse({"data": data}, safe=False)
        else:
            pokemon = Pokemon.objects.all()
            data_to_return = pokemon.values("number", "name", "image_front")
            paginator = Paginator(data_to_return, 20)
            page_number = request.GET.get('page')
            print(paginator.num_pages)
            data = list(paginator.get_page(page_number))
            data.append(paginator.num_pages)
            return JsonResponse({"data": data}, safe=False)