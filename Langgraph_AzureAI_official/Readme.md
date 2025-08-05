State Graph:-

1. It is a object defined the structure of state machine.
2. We will add nodes to represent the LLL and functions, so the appliaction can call (Tool Calling)
3. Edge:- to specify how our application should trasition between these functions.


1. When defining a graph, the first step is to define its State.
2. The State includes the graph's schema and reducer functions that handle state updates.
    a. In our example, State is a TypedDict with one key: messages.
    b. The add_messages reducer function is used to append new messages to the list instead of overwriting it. Keys without a reducer annotation will overwrite previous values.


After Generating State OurGraph can handle 2 things

1. Each Node can receive current State, as inpit and output an update to state.
2. Update to Message will ve appende to existing List rather than overrideing it, Thanks to the pre_build add_message
    function used with the Annotated Syntax.


