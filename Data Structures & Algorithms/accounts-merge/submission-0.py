class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        
    def find(self, node):
        if node != self.par[node]:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts)) # treat accounts as nodes
        
        email_to_account = {} # email -> index of account 
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in email_to_account:
                    dsu.union(email_to_account[email], i)
                else:
                    email_to_account[email] = i

        emailGroup = {} # index of account -> list of emails
        for email, i in email_to_account.items():
            parent = dsu.find(i)
            if parent not in emailGroup:
                emailGroup[parent] = []
            emailGroup[parent].append(email)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res