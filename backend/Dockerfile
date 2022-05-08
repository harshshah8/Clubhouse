FROM node:14
WORKDIR /backend
COPY --chown=node:node package*.json ./
RUN npm install
COPY --chown=node:node . ./
USER node
EXPOSE 5500
CMD [ "npm", "run", "dev" ]
