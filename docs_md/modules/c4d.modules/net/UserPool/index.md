<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/net/UserPool/index.html -->

# c4d.modules.net.UserPool <a id="c4d-modules-net-userpool"></a>

## *class* `c4d.modules.net.UserPool` <a id="c4d.modules.net.UserPool"></a>

*New in version R15.037.*

> **Warning:** This type cannot be instantiated.

## Overview <a id="overview"></a>

**Account Settings**

- [`UserPool.ChangeLanguage()`](#c4d.modules.net.UserPool.ChangeLanguage): Sets the language for a user.
- [`UserPool.ChangeUserAccountType()`](#c4d.modules.net.UserPool.ChangeUserAccountType): Changes a user’s account type.
- [`UserPool.EditUserInfo()`](#c4d.modules.net.UserPool.EditUserInfo): Sets a user’s information.

**Authentication**

- [`UserPool.ChangePassword()`](#c4d.modules.net.UserPool.ChangePassword): Changes a user’s password.
- [`UserPool.CheckUserCredentials()`](#c4d.modules.net.UserPool.CheckUserCredentials): Checks a user’s credentials.
- [`UserPool.EditUserPassword()`](#c4d.modules.net.UserPool.EditUserPassword): Sets a user’s password.

**User Management**

- [`UserPool.AddUser()`](#c4d.modules.net.UserPool.AddUser): Adds a user.
- [`UserPool.DeleteUser()`](#c4d.modules.net.UserPool.DeleteUser): Deletes a user.
- [`UserPool.GetUsers()`](#c4d.modules.net.UserPool.GetUsers): Retrieves the users information from the pool.

## Members <a id="members"></a>

### Account Settings <a id="c4d.modules.net.UserPool-method-Account-Settings"></a>

#### `UserPool.ChangeLanguage(self, userUuid, language)` <a id="c4d.modules.net.UserPool.ChangeLanguage"></a>

Sets the language for a user.

*New in version R16.021.*

**Parameters:**

- **userUuid** ([UUID](https://docs.python.org/3.9/library/uuid.html#uuid.UUID)) – The user UUID.
- **language** (*str*) – The new language.

**Return type:** bool

**Returns:** **True** if the user’s password was successfully set, otherwise **False**.

#### `UserPool.ChangeUserAccountType(self, userUuid, isAdmin)` <a id="c4d.modules.net.UserPool.ChangeUserAccountType"></a>

Changes a user’s account type.

*New in version R16.021.*

**Parameters:**

- **userUuid** – The user UUID.
- **isAdmin** (*bool*) – Set to **True** to change the user’s account type to administrator, **False** otherwise.

**Return type:** bool

**Returns:** **True** if the user’s account type was successfully changed, otherwise **False**.

#### `UserPool.EditUserInfo(self, userUuid, description)` <a id="c4d.modules.net.UserPool.EditUserInfo"></a>

Sets a user’s information.

*New in version R16.021.*

**Parameters:**

- **userUuid** – The user UUID.
- **description** (*str*) – The new user description/information.

**Return type:** bool

**Returns:** **True** if the user’s information was successfully set, otherwise **False**.

### Authentication <a id="c4d.modules.net.UserPool-method-Authentication"></a>

#### `UserPool.ChangePassword(self, userUuid, oldPassword, newPassword)` <a id="c4d.modules.net.UserPool.ChangePassword"></a>

Changes a user’s password.

**Parameters:**

- **userUuid** –

  *New in version R16.021:* The user UUID.

- **oldPassword** (*str*) – The old user’s password.

- **newPassword** (*str*) – The new user’s password.

**Return type:** bool

**Returns:** **True** if the user’s password was successfully changed, otherwise **False**.

#### `UserPool.CheckUserCredentials(self, username, password)` <a id="c4d.modules.net.UserPool.CheckUserCredentials"></a>

Checks a user’s credentials.

**Parameters:**

- **username** (*str*) – The user name.
- **password** (*str*) – The user password.

**Return type:** bool

**Returns:** **True** if the user’s credentials were successfully checked, otherwise **False**.

#### `UserPool.EditUserPassword(self, userUuid, password)` <a id="c4d.modules.net.UserPool.EditUserPassword"></a>

Sets a user’s password.

*New in version R16.021.*

**Parameters:**

- **userUuid** – The user UUID.
- **password** (*str*) – The new password.

**Return type:** bool

**Returns:** **True** if the user’s password was successfully set, otherwise **False**.

### User Management <a id="c4d.modules.net.UserPool-method-User-Management"></a>

#### `UserPool.AddUser(self, username, password, description, isAdmin)` <a id="c4d.modules.net.UserPool.AddUser"></a>

Adds a user.

**Parameters:**

- **username** (*str*) – The user’s name.
- **password** (*str*) – The user’s password.
- **description** (*str*) – The user’s description.
- **isAdmin** (*bool*) – Set to **True** if the user to add is administrator, **False** otherwise.

**Return type:** bool

**Returns:** **True** if the user was successfully added, **False** otherwise.

#### `UserPool.DeleteUser(self, userUuid)` <a id="c4d.modules.net.UserPool.DeleteUser"></a>

Deletes a user.

**Parameters:**

**userUuid** –

*New in version R16.021:* The user UUID.

**Return type:** bool

**Returns:** **True** if the user was successfully deleted, **False** otherwise.

#### `UserPool.GetUsers(self)` <a id="c4d.modules.net.UserPool.GetUsers"></a>

Retrieves the users information from the pool.

*New in version R16.021.*

**Return type:** List[Dict[**username**, str, **description**: str, **uuid**: [UUID](https://docs.python.org/3.9/library/uuid.html#uuid.UUID), , **isadmin**: bool, **language**: str]]

**Returns:** The users information.
