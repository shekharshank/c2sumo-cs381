FROM grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild
# make necessary directories/files and set the permissions appropriately
RUN mkdir -p /app/Middleware/log
RUN mkdir -p /app/Middleware/session
RUN mkdir -p /app/Middleware/static/Data
RUN chown -hR www-data /app/Middleware/log /app/Middleware/session /app/Middleware/static/Data
RUN chmod +x .whiskey/action_hooks/deploy
CMD ["Middleware/c3stemserver.py"]
