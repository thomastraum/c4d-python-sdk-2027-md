<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.IdProvider.html -->

# mxutils.IdProvider <a id="mxutils-idprovider"></a>

## Description <a id="module-mxutils.IdProvider"></a><a id="description"></a>

Generates `int` or `maxon.Id` identifiers.

A provider can yield identifiers in multiple scopes, where generation is independent and continuous for each scope.

> **Note:**
>
> `mxutils.g_id_provider` is a global instance of this class that can be used directly. It yields `int` IDs.

**Example:**

```python
# An IdProvider can be used in any situation where either integer or maxon.Id identifiers
# are required but one does not care too much about the exact makeup of each ID.

# Providers can be initialized for one of the ID types, the default is `int`.
intProvider: IdProvider = IdProvider(int)
maxonProvider: IdProvider = IdProvider(maxon.Id)

# A provider can use scopes/namespaces for generating IDs to provide multiple sets of IDs. 
# A scope can either be an integer or a string. 
scopeA: int = 0
scopeB: str = 'net.my-company.com.product.ids'

# The property IdType will return the type of IDs yielded by an instance.
print(f'{intProvider.IdType = }') # Will print <class 'int'>
print(f'{maxonProvider.IdType = }') # Will print <class 'maxon.data.Id'>

# With Get() a new ID is being yielded for the given scope. Providing no scope will
# place the ID in the default scope. When a new scope is opened by passing a scope 
# identifier for the first time, the first ID will be 1000 unless a different startValue 
# is being provided.

print(f'{intProvider.Get() = }')               # 1000
print(f'{intProvider.Get(scopeA) = }')         # 1000
print(f'{intProvider.Get(scopeB, 2000) = }')   # 2000
print(f'{maxonProvider.Get() = }')             # maxon.Id('net.maxon.namespace.user.default#1000')
print(f'{maxonProvider.Get(scopeA) = }')       # maxon.Id('1000#1000')
print(f'{maxonProvider.Get(scopeB, 2000) = }') # maxon.Id('net.my-company.com.product.ids#2000')

# Subsequent calls to Get() will yield the next ID in the sequence for the given scope.

print(f'{intProvider.Get() = }')               # 1001
print(f'{intProvider.Get() = }')               # 1002
print(f'{intProvider.Get(scopeA) = }')         # 1001
print(f'{intProvider.Get(scopeB) = }')         # 2001

print(f'{maxonProvider.Get() = }')             # maxon.Id('net.maxon.namespace.user.default#1001')
print(f'{maxonProvider.Get() = }')             # maxon.Id('net.maxon.namespace.user.default#1002')
print(f'{maxonProvider.Get(scopeA) = }')       # maxon.Id('1000#1001')
print(f'{maxonProvider.Get(scopeB) = }')       # maxon.Id('net.my-company.com.product.ids#2001')

# GetLast() returns the last ID which has been yielded for a scope and GetAll() returns
# all of them.

print(f'{intProvider.GetLast() = }')         # 1002
print(f'{intProvider.GetLast(scopeA) = }')   # 1001
print(f'{maxonProvider.GetLast() = }')       # maxon.Id('net.maxon.namespace.user.default#1002')
print(f'{maxonProvider.GetLast(scopeA) = }') # maxon.Id('1000#1001')

print(f'{intProvider.GetAll() = }')          # (1000, 1001, 1002)
print(f'{intProvider.GetAll(scopeA) = }')    # (1000, 1001)
print(f'{maxonProvider.GetAll() = }')        # (maxon.Id('net.maxon.namespace.user.default#1000'),
                                             #  maxon.Id('net.maxon.namespace.user.default#1001'),
                                             #  maxon.Id('net.maxon.namespace.user.default#1002'))
print(f'{maxonProvider.GetAll(scopeA) = }')  # (maxon.Id('1000#1000'), 
                                             #  maxon.Id('1000#1001'))
```

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`mxutils.IdProvider.DEFAULT_SCOPE`](mxutils.IdProvider.DEFAULT_SCOPE.md#mxutils.IdProvider.DEFAULT_SCOPE) | The scope which is used when no scope is being provided. |
| [`mxutils.IdProvider.ID_TYPES`](mxutils.IdProvider.ID_TYPES.md#mxutils.IdProvider.ID_TYPES) | Contains all valid identifier types this class can handle. |
| [`mxutils.IdProvider.IdType`](mxutils.IdProvider.IdType.md#mxutils.IdProvider.IdType) | Returns the type of identifiers managed by the instance. |
| [`mxutils.IdProvider.Scopes`](mxutils.IdProvider.Scopes.md#mxutils.IdProvider.Scopes) | Returns all scope identifiers managed by the instance. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Get`](#mxutils.IdProvider.Get)([scope, startValue]) | Returns the next identifier for the given `scope`. |
| [`GetAll`](#mxutils.IdProvider.GetAll)([scope]) | Returns all identifiers that have been generated for the given `scope`. |
| [`GetLast`](#mxutils.IdProvider.GetLast)([scope]) | Returns the last identifier which has been yielded for the given `scope`. |
| [`__init__`](#mxutils.IdProvider.__init__)([idType]) | Initializes the provider with an identifier type. |

## Methods Definition <a id="methods-definition"></a>

### `IdProvider.Get(scope: int | str | None = None, startValue: int = 1000) → int | maxon.data.Id` <a id="mxutils.IdProvider.Get"></a>

Returns the next identifier for the given `scope`.

**Parameters:** **scope** (*int | str | None* (, *optional*)) – The scope symbol to get a new identifier for. When a never before seen scope is passed, a new entry will be created with `startValue` as the starting value. Passing `None` will use `IdProvider.DEFAULT_SCOPE`. Defaults to `None`.

**Raises:** **TypeError** – On invalid argument types.

**Returns:** A newly created identifier which is unique within the given scope.

**Return type:** int | maxon.Id

### `IdProvider.GetAll(scope: int | str | None = None) → tuple[int, …] | tuple[maxon.data.Id, …]` <a id="mxutils.IdProvider.GetAll"></a>

Returns all identifiers that have been generated for the given `scope`.

**Parameters:** **scope** (*int | str | None* (, *optional*)) – The scope symbol to get all identifiers for. Passing `None` will use `IdProvider.DEFAULT_SCOPE`. Defaults to `None`.

**Raises:**

- **TypeError** – On invalid argument types.
- **IndexError** – When `scope` does not exist.

**Returns:** All identifiers which have been yielded for `scope`. Can be the empty tuple.

**Return type:** tuple[int, ..] | tuple[maxon.Id, ..]

### `IdProvider.GetLast(scope: int | str | None = None) → int | maxon.data.Id` <a id="mxutils.IdProvider.GetLast"></a>

Returns the last identifier which has been yielded for the given `scope`.

**Parameters:** **scope** (*int | str | None* (, *optional*)) – The scope symbol to get a new identifier for. Passing `None` will use `IdProvider.DEFAULT_SCOPE`. Defaults to `None`.

**Raises:**

- **TypeError** – On invalid argument types.
- **IndexError** – When `scope` does not exist or has no elements.

**Returns:** The last identifier which has been yielded for `scope`.

**Return type:** int | maxon.Id

### `IdProvider.__init__(idType: Type = <class 'int'>) → None` <a id="mxutils.IdProvider.__init__"></a>

Initializes the provider with an identifier type.

**Parameters:** **idType** (*int*) – The type of IDs the provider should handle. The value must lie within `IdProvider.ID_TYPES`. Defaults to `int`.

**Raises:** **ValueError** – When `idType` does not lie within `IdProvider.ID_TYPES`.
