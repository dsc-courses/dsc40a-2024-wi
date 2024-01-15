.PHONY: preview

preview:
	bundle exec jekyll serve & sleep 4 && open http://127.0.0.1:4000
