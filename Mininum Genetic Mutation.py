from collections import deque

def minMutation(start: str, end: str, bank: List[str]) -> int:
    # Create a set to store the valid gene bank
    gene_bank = set(bank)
    
    # Create a queue to perform BFS
    queue = deque([(start, 0)])
    
    # Create a set to store visited genes
    visited = set([start])
    
    # Define the possible mutations
    mutations = {'A', 'C', 'G', 'T'}
    
    while queue:
        gene, steps = queue.popleft()
        
        # If we reach the end gene, return the number of steps
        if gene == end:
            return steps
        
        # Iterate through each character in the gene
        for i in range(len(gene)):
            for mutation in mutations:
                # Generate a new gene by replacing the character at index i
                new_gene = gene[:i] + mutation + gene[i+1:]
                
                # Check if the new gene is in the gene bank and not visited
                if new_gene in gene_bank and new_gene not in visited:
                    # Add the new gene to the queue and mark it as visited
                    queue.append((new_gene, steps + 1))
                    visited.add(new_gene)
    
    # If there is no valid mutation path, return -1
    return -1