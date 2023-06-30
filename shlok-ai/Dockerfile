FROM node:18.16.0 as build-stage

# Create app directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./
RUN npm install
# Bundle app source
COPY . .
RUN npm run build

# If you are building your code for production
# RUN npm ci --omit=dev

FROM nginx:1.25.0-alpine as prod-stage
COPY --from=build-stage /app/build /usr/share/nginx/html
RUN mkdir /etc/nginx/conf.d/letsencrypt
# EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]

# EXPOSE 8080
# CMD [ "node", "./src/components/Main.js" ]