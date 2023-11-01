wget --quiet \
	--method GET \
	--header 'X-RapidAPI-Key: SIGN-UP-FOR-KEY' \
	--header 'X-RapidAPI-Host: heisenbug-la-liga-live-scores-v1.p.rapidapi.com' \
	--output-document \
	- 'https://heisenbug-la-liga-live-scores-v1.p.rapidapi.com/api/laliga/team?name=Real%20Madrid'