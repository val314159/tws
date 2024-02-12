FROM alpine:3.19
RUN apk add make emacs-nox coreutils py-docopt nodejs npm
RUN npm i -g postcss autoprefixer tailwindcss daisyui vite
ADD . /
WORKDIR /x
