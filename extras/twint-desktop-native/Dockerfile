FROM mhart/alpine-node 

RUN apk add --no-cache git && \
	yarn global add react-native exp react-native-cli

COPY . /opt/ui
WORKDIR /opt/ui

RUN npm install 