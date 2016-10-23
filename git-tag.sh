#!/bin/bash
if [ "$TRAVIS_BRANCH" == "master" ]; then
  if [ "${ghToken:-false}" != "false" ]; then
    git config --global user.email "tomaszguzialek_flask-api@travis-ci.org"
    git config --global user.name "Travis CI"
    export GIT_TAG=build-$TRAVIS_BUILD_NUMBER
    git tag $GIT_TAG -a -m "Generated tag from TravisCI build $TRAVIS_BUILD_NUMBER"
    git push -q https://$TAG_GENERATION_ACCESS_TOKEN@github.com/tomaszguzialek/flask-api.git --tags
    echo Created and pushed tag $GIT_TAG
  else
    echo Skipping creating the tag as the build is a pull request push
  fi
else
  echo Skipping creating the tag as the build is not on master branch
fi
