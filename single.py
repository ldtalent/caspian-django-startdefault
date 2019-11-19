from django.conf import settings
from django.http import HttpResponse

settings.configure(
	DEBUG = True,
	SECRET_KEY = 'LetsUseThisForNow.WeWillTakeCareOfThisLater',
	ROOT_URLCONF = __name__,
	MIDDLEWARE_CLASSES = [
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
	],
)

def index(request):
	return HttpResponse("<h1>Hello, this is a minimal project setup. Configure as you please!</h1>")
