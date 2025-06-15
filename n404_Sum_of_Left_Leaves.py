class Solution(object):
    def sumOfLeftLeaves(self, root):
        
        if not root:
            return 0

        total = 0

        if root.left:
         
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                # Рекурсивно обробляємо ліву гілку
                total += self.sumOfLeftLeaves(root.left)

        total += self.sumOfLeftLeaves(root.right)

        return total