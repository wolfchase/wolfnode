def static_vars(request):
    return {
        'pages':  [
            {'link': '/about', 'name': 'about'},
            {'link': '/resume', 'name': 'resume'},
            {'link': '/projects', 'name': 'projects'},
            {'link': '/contact', 'name': 'contact'},
            {'link': '/archive', 'name': 'archive'},
        ],
    }
