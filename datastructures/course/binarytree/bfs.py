def bfs(self, data):
        if self.root is None:
            return False
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.val)
            if node.val == data:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

