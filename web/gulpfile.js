//Dependencias
var browserSync = require('browser-sync');
var concatCSS   = require('gulp-concat-css');
var concatJS    = require('gulp-concat');
var del         = require('del');
var gulp        = require('gulp');
var minifyCSS   = require('gulp-minify-css');
var minifyHTML  = require('gulp-minify-html');
var minifyJS    = require('gulp-uglify');
var reload      = browserSync.reload;
var rename      = require('gulp-rename');
var stylus      = require('gulp-stylus');
var jshint      = require('gulp-jshint');

//Archivos a copiar a dist

var _PROYECTOJS = [
    'app/app.module.js',
    'app/app.routes.js',
    'app/shared/**/*.js',
    'app/components/**/*.js',
    'assets/js/**/*.js'
];

var _HTML = [
    'app/shared/**/*.html', 
    'app/components/**/*.html'
];

var _STYLUS = 'assets/stylus/**/*.styl';

//Solo las dependencias
var _CSS = [
    'assets/libs/mdi/css/**/*.min.*',
    'assets/libs/angular-material/angular-material.min.css'
];

//Solo las dependencias
var _JAVASCRIPT = [
	'assets/libs/jquery/dist/*.min.*',
    'assets/libs/angular/*.min.*',
    'assets/libs/angular-route/*.min.*',
	'assets/libs/ngInfiniteScroll/build/*.min.*',
    'assets/libs/moment/min/*.min.*',
    'assets/libs/angular-animate/*.min.*',
    'assets/libs/angular-aria/*.min.*',
    'assets/libs/angular-material/angular-material.min.js'
];

//Todas las fuentes tanto tuyas como de dependencias
var _FONTS = [
    'assets/fonts/**/*',
    'assets/libs/mdi/fonts/**/*'
];

//Todas las imagenes tanto tuyas como de dependencias
var _IMGS = [
  	'assets/img/**/*'
];

var _BASE = [
	'index.html'
];

//Tareas
gulp.task('minify-css', function () {
    gulp.src(_STYLUS)
    .pipe(stylus())
    .pipe(concatCSS('style.min.css'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('dist/assets/css'))
    .pipe(reload({stream: true, once: true}));
});

gulp.task('minify-js', function () {
    gulp.src(_PROYECTOJS)
    .pipe(concatJS('main.min.js'))
    .pipe(minifyJS())
    .pipe(gulp.dest('dist/assets/js'))
    .pipe(reload({stream: true, once: true}));
});

gulp.task('lint', function () {
    gulp.src(_PROYECTOJS)
    .pipe(jshint())
    .pipe(jshint.reporter('jshint-stylish'));
});

gulp.task('minify-html', function () {
    gulp.src(_HTML)
    .pipe(rename({suffix: '.min'}))
    .pipe(minifyHTML())
    .pipe(gulp.dest('dist/templates'))
    .pipe(reload({stream: true, once: true}));
});

gulp.task('copyBase', function(){
	gulp.src(_BASE)
    .pipe(gulp.dest('dist'));
});


gulp.task('copyCss', function(){
	gulp.src(_CSS)
    .pipe(gulp.dest('dist/assets/css'));
});


gulp.task('copyJs', function(){
	gulp.src(_JAVASCRIPT)
    .pipe(gulp.dest('dist/assets/js'));
});


gulp.task('copyImgs', function(){
	gulp.src(_IMGS)
    .pipe(gulp.dest('dist/assets/img'));
});

gulp.task('copyFonts', function(){
	gulp.src(_FONTS)
    .pipe(gulp.dest('dist/assets/fonts'));
});


gulp.task('watch', function() {
    // Cambios principales
    gulp.watch(_PROYECTOJS, ['lint', 'minify-js']);
    gulp.watch(_STYLUS,     ['minify-css']);
    gulp.watch(_HTML,       ['minify-html']);
});

gulp.task('server-start', function () {
    browserSync({
        notify: false,
        server: 'dist/'
    });
});


//Tareas IMPORTANTES

gulp.task('debug', function() {
    gulp.start('lint');
});

gulp.task('dist', ['clean'], function() {
    gulp.start('copyBase', 'copyCss', 'copyJs', 'copyImgs', 'copyFonts', 'minify-css', 'minify-html', 'minify-js', 'lint');
});

gulp.task('server', function() {
    gulp.start('lint', 'server-start', 'watch');
});

gulp.task('clean', function(cb) {
    del(['dist'], cb);
});
