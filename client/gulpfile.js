var gulp = require('gulp');
var gutil = require('gulp-util');
var bower = require('bower');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var jetpack      = require('fs-jetpack');
var usemin       = require('gulp-usemin');
var uglify       = require('gulp-uglify');
var minifyHtml   = require('gulp-minify-html');
var minifyCss = require('gulp-minify-css');
var rev          = require('gulp-rev');
var rename = require('gulp-rename');
var sh = require('shelljs');

var projectDir   = jetpack;
var clientDir    = projectDir.cwd('./client');
var cordovaDir     = projectDir.cwd('./cordova-build');
var cordovaClientDir     = projectDir.cwd('./cordova-build/www');
var electronDir      = projectDir.cwd('./electron-build');
var paths = {
  sass: ['./client/scss/**/*.scss']
};


///////////////
// Sass Tasks
///////////////
gulp.task('sass', function(done) {
  gulp.src('./client/scss/ionic.app.scss')
    .pipe(sass())
    .on('error', sass.logError)
    .pipe(gulp.dest('./www/css/'))
    .pipe(minifyCss({
      keepSpecialComments: 0
    }))
    .pipe(rename({ extname: '.min.css' }))
    .pipe(gulp.dest('./www/css/'))
    .on('end', done);
});

gulp.task('watch', function() {
  gulp.watch(paths.sass, ['sass']);
});


///////////////
// Cordova Tasks
///////////////
gulp.task('clean-cordova', function () {
  return cordovaClientDir.dirAsync('.', { empty: true });
});

gulp.task('copy-cordova', ['clean-cordova'], function () {
  return projectDir.copy(clientDir.path(), cordovaClientDir.path(), {
    overwrite: true, matching: [
      '*.*',
      '**/*.**'
    ]
  });
});

gulp.task('copy-npm-cordova', ['copy-cordova'], function () {
  return projectDir.copy(clientDir.path(), cordovaDir.path(), {
    overwrite: true, matching: [
      "node_modules/**.*"
    ]
  });
});

gulp.task('build-cordova', ['copy-npm-cordova']);

////////////
// Electron Tasks
////////////
gulp.task('clean-electron', function () {
  return electronDir.dirAsync('.', { empty: true });
});

gulp.task('copy-electron', ['clean-electron'], function () {
  return projectDir.copy(clientDir.path(), electronDir.path(), {
    overwrite: true, matching: [
      '*.*',
      '**/*.**'
    ]
  });
});

gulp.task('build-electron', ['copy-electron']);


gulp.task('build-all', ['build-cordova', 'build-electron']);
