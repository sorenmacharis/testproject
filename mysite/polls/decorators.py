from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    #gebruiker moet deel uitmaken van minstens één van de opgegeven groepen
    def in_groups(u):
        
        if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
            return True
        return False

    return user_passes_test(in_groups, login_url='/accounts/logout')


