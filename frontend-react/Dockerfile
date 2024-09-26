FROM node:20-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
# CMD ["sh", "-c", "HOST=0.0.0.0 npm start"]