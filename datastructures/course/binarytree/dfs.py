def dfs(self, data):
        return self._dfs_recursive(self.root, data)

def _dfs_recursive(self, node, data):
    if node:
        print(node.val)
    if node is None:
        return False
    if node.val == data:
        return True
    if self._dfs_recursive(node.left, data):
        return True
    if self._dfs_recursive(node.right, data):
        return True