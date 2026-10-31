<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/datatype/maxon.GraphTransaction.html -->

# maxon.GraphTransaction <a id="maxon-graphtransaction"></a>

## Description <a id="module-maxon.GraphTransaction"></a><a id="description"></a>

Modifications to a GraphModelInterface may only be done when there is an active GraphTransaction.

You start a transaction by calling `GraphModelInterface.BeginTransaction()` on the graph to modify. When all modifications are done, you call `GraphTransaction.Commit()` to make them permanent, or `GraphTransaction.Rollback()` to return to the state of the graph when `GraphModelInterface.BeginTransaction()` has been called.

> **Note:** Transactions can be nested and a commit or rollback ends the current (innermost) transaction, but not enclosing transactions.

If a GraphTransaction goes out of scope but is still active (`GraphTransaction.Commit()` or `GraphTransaction.Rollback()` hasn’t been called), a rollback is triggered implicitly by the destructor. This is important for error handling, as it implies that in case of an unhandled error an implicit rollback is made. This prevents inconsistent states of the graph.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)
- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Commit`](#maxon.GraphTransaction.Commit)([userData]) | Commits (end ends) this transaction. |
| [`GetGraph`](#maxon.GraphTransaction.GetGraph)() | Returns the graph of this transaction, or a null reference when this transaction is inactive. |
| [`IsActive`](#maxon.GraphTransaction.IsActive)() | Checks if this transaction is active. |
| [`Rollback`](#maxon.GraphTransaction.Rollback)() | Rolls back the graph to its state at the time this transaction has been started, and ends this transaction. |
| [`__del__`](#maxon.GraphTransaction.__del__)() |  |
| [`__enter__`](#maxon.GraphTransaction.__enter__)() |  |
| [`__exit__`](#maxon.GraphTransaction.__exit__)(exc_type, exc_val, exc_tb) |  |
| [`__init__`](#maxon.GraphTransaction.__init__)([src]) | Initializes a transaction. |

## Methods Definition <a id="methods-definition"></a>

### `GraphTransaction.Commit(userData=None)` <a id="maxon.GraphTransaction.Commit"></a>

Commits (end ends) this transaction.  
The changes made within this transaction become permanent in the graph (unless this is a nested transaction and an enclosing transaction is rolled back later).  
If this transaction isn’t active, nothing happens.

**Parameters:**

**userData** (*maxon.DataDictionary*) –

User data to pass to the observers of GraphModelInterface.ObservableTransactionCommitted.  
This will be merged with all given user data of nested commits.

### `GraphTransaction.GetGraph()` <a id="maxon.GraphTransaction.GetGraph"></a>

Returns the graph of this transaction, or a null reference when this transaction is inactive.

**Return type:** [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)

**Returns:** Graph of transaction, or null reference.

### `GraphTransaction.IsActive()` <a id="maxon.GraphTransaction.IsActive"></a>

Checks if this transaction is active.  
A transaction is active between the initial call to [`GraphModelInterface.BeginTransaction()`](../interface/maxon.GraphModelInterface.md#maxon.GraphModelInterface.BeginTransaction) and the corresponding call to `GraphModelInterface.Commit()` or `GraphModelInterface.Rollback()`.

**Return type:** [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)

**Returns:** **True** if this transaction is active otherwise **False**

### `GraphTransaction.Rollback()` <a id="maxon.GraphTransaction.Rollback"></a>

Rolls back the graph to its state at the time this transaction has been started, and ends this transaction.

### `GraphTransaction.__del__()` <a id="maxon.GraphTransaction.__del__"></a>

### `GraphTransaction.__enter__()` <a id="maxon.GraphTransaction.__enter__"></a>

### `GraphTransaction.__exit__(exc_type, exc_val, exc_tb)` <a id="maxon.GraphTransaction.__exit__"></a>

### `GraphTransaction.__init__(src=None)` <a id="maxon.GraphTransaction.__init__"></a>

Initializes a transaction.

**Parameters:** **src** ([`maxon.GraphTransaction`](#module-maxon.GraphTransaction)) – An optional transaction to re-use.
