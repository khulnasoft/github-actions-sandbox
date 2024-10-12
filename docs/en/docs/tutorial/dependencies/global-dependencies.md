# Global Dependencies

For some types of applications you might want to add dependencies to the whole application.

Similar to the way you can [add `dependencies` to the _path operation decorators_](dependencies-in-path-operation-decorators.md){.internal-link target=\_blank}, you can add them to the `ReadyAPI` application.

In that case, they will be applied to all the _path operations_ in the application:

=== "Python 3.9+"

    ```Python hl_lines="16"
    {!> ../../../docs_src/dependencies/tutorial012_an_py39.py!}
    ```

=== "Python 3.6+"

    ```Python hl_lines="16"
    {!> ../../../docs_src/dependencies/tutorial012_an.py!}
    ```

=== "Python 3.6 non-Annotated"

    !!! tip
        Prefer to use the `Annotated` version if possible.

    ```Python hl_lines="15"
    {!> ../../../docs_src/dependencies/tutorial012.py!}
    ```

And all the ideas in the section about [adding `dependencies` to the _path operation decorators_](dependencies-in-path-operation-decorators.md){.internal-link target=\_blank} still apply, but in this case, to all of the _path operations_ in the app.

## Dependencies for groups of _path operations_

Later, when reading about how to structure bigger applications ([Bigger Applications - Multiple Files](../../tutorial/bigger-applications.md){.internal-link target=\_blank}), possibly with multiple files, you will learn how to declare a single `dependencies` parameter for a group of _path operations_.