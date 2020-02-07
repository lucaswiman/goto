.PHONY: serve
serve: schema
	./bookmark serve


.PHONY: schema
schema: bookmarks.db
	./bookmark create-schema
