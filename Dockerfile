FROM baserow/baserow:1.19.1

# Set environment variables
ENV BASEROW_PUBLIC_URL="http://mskwo0gws0c8owwsswkc0c0k.104.37.187.180.sslip.io"
ENV BASEROW_CADDY_ADDRESSES=":80"
ENV BASEROW_ENABLE_SECURE_PROXY_HEADERS="true"
ENV BASEROW_EXTRA_ALLOWED_HOSTS="*"

EXPOSE 80
EXPOSE 443

CMD ["/baserow/startup.sh"]
