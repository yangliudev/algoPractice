1. What is Angular?
Angular is a TypeScript based open source web application framework developed by Google.

2. State some advantages of Angular over other frameworks
Angular has useful built in features such as routing, state management, HTTP services.
It has long term Google support.
Uses Declarative UI, which means that Angular html to render the UI of an application. HTML is a declarative language and is much easier to use than JavaScript.

3. What are Lifecycle hooks in Angular? Explain some life cycles hooks

Every component in Angular has a lifecycle, these are different phases that it goes through from the time it is created to the time that it is destroyed. We use hooks to tap into any of these phases.

ngOnChanges() - this method is called whenever one or more input properties of the component changes (called before ngOnInit())
ngOnInit() - this hook gets called once after the ngOnChanges hook. it initliazes the component and sets the input properties of the component
ngDoCheck() - this is called after ngOnChanges() and ngOnInit() it is used to detect and act on changes that cannot be deteced by Angular.

ngOnDestroy() - this gets called before Angular destroys the component. This hook can be used to clean up the code and detach event handlers.

4. Describe the MVC architecture
Model - manages application data, it responds to the request from the view 
View - displays the data to the user
Controller - code that controls the interactions between the model and view

5. What is ViewModel?
Acts as a bridge between the View and the Model

6. What is @NgModule?
The NgModule class describes how the application parts fit together

6. Directive types in Angular?

    3 types of directives
        1. Structural Directives - changes the DOM layout by adding removing DOM elements. (ie: *ngIf *ngFor)
        2. Attribute Directives - changes the appearance or behavior of an element. (*ngStyle *ngClass)
        3. Components - directives with a template

7. What are the uses of a service in Angular?
Services focus on functionality. 

8. What is Redux?
Redux is an application manager for JavaScript Applications

9. Why were client-side frameworks like Angular introduced?
Angular made development easier by separating concerns and dividing the code into smaller bits of information called components

10. How does an Angular application work?
The most important part of an Angular application is the angular.json file. This file contains all the neccessary configurations of the app.

11. Differences between AngularJS and Angular?
The first main differnce is that Angular is a complete rewrite from AngularJS. So Angular is newer and mainted by Google while AngularJS is old and not supported anymore. AngularJS as you can tell by the name uses js while Angular uses typescript.
So essentially to sum it up, Angular is everything that's good about angularjs but even better.

12. AOT vs JIT
AOT stands for ahead of time and when compiled in AOT, it compiles during the build time.
JIT stands for just in time and when compiled in JIT, it compiles inside of the browser during the runtime.

13. Components, Modules, Services
Components are the building blocks that comprise the application. It is defined using the @Component decorator.
Modules are a place where you can group components, directives, services, and pipes