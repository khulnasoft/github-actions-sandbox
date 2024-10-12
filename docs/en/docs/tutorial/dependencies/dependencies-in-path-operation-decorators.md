# Dependencies in path operation decorators

In some cases you don't really need the return value of a dependency inside your _path operation function_.

Or the dependency doesn't return a value.

But you still need it to be executed/solved.

For those cases, instead of declaring a _path operation function_ parameter with `Depends`, you can add a `list` of `dependencies` to the _path operation decorator_.

## Add `dependencies` to the _path operation decorator_

The _path operation decorator_ receives an optional argument `dependencies`.

It should be a `list` of `Depends()`:

=== "Python 3.9+"

    ```Python hl_lines="19"
    {!> ../../../docs_src/dependencies/tutorial006_an_py39.py!}
    ```

=== "Python 3.6+"

    ```Python hl_lines="18"
    {!> ../../../docs_src/dependencies/tutorial006_an.py!}
    ```

=== "Python 3.6 non-Annotated"

    !!! tip
        Prefer to use the `Annotated` version if possible.

    ```Python hl_lines="17"
    {!> ../../../docs_src/dependencies/tutorial006.py!}
    ```

These dependencies will be executed/solved the same way normal dependencies. But their value (if they return any) won't be passed to your _path operation function_.

!!! tip
Some editors check for unused function parameters, and show them as errors.

    Using these `dependencies` in the *path operation decorator* you can make sure they are executed while avoiding editor/tooling errors.

    It might also help avoid confusion for new developers that see an unused parameter in your code and could think it's unnecessary.

!!! info
In this example we use invented custom headers `X-Key` and `X-Token`.

    But in real cases, when implementing security, you would get more benefits from using the integrated [Security utilities (the next chapter)](../security/index.md){.internal-link target=_blank}.

## Dependencies errors and return values

You can use the same dependency _functions_ you use normally.

### Dependency requirements

They can declare request requirements (like headers) or other sub-dependencies:

=== "Python 3.9+"

    ```Python hl_lines="8  13"
    {!> ../../../docs_src/dependencies/tutorial006_an_py39.py!}
    ```

=== "Python 3.6+"

    ```Python hl_lines="7  12"
    {!> ../../../docs_src/dependencies/tutorial006_an.py!}
    ```

=== "Python 3.6 non-Annotated"

    !!! tip
        Prefer to use the `Annotated` version if possible.

    ```Python hl_lines="6  11"
    {!> ../../../docs_src/dependencies/tutorial006.py!}
    ```

### Raise exceptions

These dependencies can `raise` exceptions, the same as normal dependencies:

=== "Python 3.9+"

    ```Python hl_lines="10  15"
    {!> ../../../docs_src/dependencies/tutorial006_an_py39.py!}
    ```

=== "Python 3.6+"

    ```Python hl_lines="9  14"
    {!> ../../../docs_src/dependencies/tutorial006_an.py!}
    ```

=== "Python 3.6 non-Annotated"

    !!! tip
        Prefer to use the `Annotated` version if possible.

    ```Python hl_lines="8  13"
    {!> ../../../docs_src/dependencies/tutorial006.py!}
    ```

### Return values

And they can return values or not, the values won't be used.

So, you can re-use a normal dependency (that returns a value) you already use somewhere else, and even though the value won't be used, the dependency will be executed:

=== "Python 3.9+"

    ```Python hl_lines="11  16"
    {!> ../../../docs_src/dependencies/tutorial006_an_py39.py!}
    ```

=== "Python 3.6+"

    ```Python hl_lines="10  15"
    {!> ../../../docs_src/dependencies/tutorial006_an.py!}
    ```

=== "Python 3.6 non-Annotated"

    !!! tip
        Prefer to use the `Annotated` version if possible.

    ```Python hl_lines="9  14"
    {!> ../../../docs_src/dependencies/tutorial006.py!}
    ```

## Dependencies for a group of _path operations_

Later, when reading about how to structure bigger applications ([Bigger Applications - Multiple Files](../../tutorial/bigger-applications.md){.internal-link target=\_blank}), possibly with multiple files, you will learn how to declare a single `dependencies` parameter for a group of _path operations_.

## Global Dependencies

Next we will see how to add dependencies to the whole `ReadyAPI` application, so that they apply to each _path operation_.