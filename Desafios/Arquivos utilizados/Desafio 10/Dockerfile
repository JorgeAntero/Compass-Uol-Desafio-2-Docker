FROM node:alpine
RUN adduser -S Jorge
WORKDIR /app
COPY . .
USER Jorge
EXPOSE 3000
CMD ["node", "index.js"]