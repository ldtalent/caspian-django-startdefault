from django.conf import settings

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