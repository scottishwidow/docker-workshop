FROM node:20-alpine as builder

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

FROM node:18-apline

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 3000

CMD ["node", "index.js"]
