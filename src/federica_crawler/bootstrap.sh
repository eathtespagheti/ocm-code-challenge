#!/usr/bin/env sh

[ -z "$FIRSTRUN_CHECKFILE" ] && FIRSTRUN_CHECKFILE="firstrun"

# If FIRSTRUN_CHECKFILE doesn't exist
[ ! -f "$FIRSTRUN_CHECKFILE" ] && {
    django-admin collectstatic --noinput
    django-admin migrate --noinput
    adminPassword=$(cat /run/secrets/django-admin-password)

    # if both ADMIN_NAME and adminPassword exists
    [ -n "$ADMIN_NAME" ] && [ -n "$adminPassword" ] && {
        echo "from django.contrib.auth.models import User; User.objects.create_superuser('$ADMIN_NAME', '$ADMIN_EMAIL', '$adminPassword')" | django-admin shell
    }
    touch "$FIRSTRUN_CHECKFILE"
}

django-admin runserver 0.0.0.0:8000