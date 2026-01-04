CREATE (:Agent {id: 'agent-1', name: 'Sample Agent 1'});
CREATE (:Operation {id: 'op-1', name: 'Initial operation', description: 'Seed operation for demonstration'});
CREATE (:Operation {id: 'op-2', name: 'Second operation', description: 'Another operation'});
MATCH (a:Agent {id:'agent-1'}), (o:Operation {id:'op-1'}) CREATE (a)-[:CAN_EXECUTE]->(o);
MATCH (a:Agent {id:'agent-1'}), (o:Operation {id:'op-2'}) CREATE (a)-[:CAN_EXECUTE]->(o);
