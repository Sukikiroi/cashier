const { useState } = owl.hooks;

class MyComponent extends Component {
    setup() {
        // initialize component here
        console.log("I am OWL")
        state = { value: 0 };
    }
}
MyComponent.template = 'myaddon.MyComponent';