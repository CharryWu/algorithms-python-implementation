# https://leetcode.com/problems/regular-expression-matching/
import string
class Solution():
    def isMatch(self, s: str, p: str) -> bool:
        STATE_MACHINE = []
        STARTING_STATE = 0
        ACCEPT_STATE = len(p)
        FAIL_STATE = len(p)+1

        # Build NFA from pattern string
        for i, c in enumerate(p):
            nextState = i+1
            if c == '.':
                STATE_MACHINE.append({ x: {nextState} for x in string.ascii_lowercase})
            elif c == '*':
                prev_state = STATE_MACHINE[-1]
                for trans in prev_state:
                    prev_state[trans].add(nextState)
                prev_state['*'] = {nextState} # setup '*' for skipping the prev char entirely
                STATE_MACHINE.append(prev_state)
            else:
                STATE_MACHINE.append({ c: {nextState}})

        STATE_MACHINE.append({ x: {FAIL_STATE} for x in string.ascii_lowercase+'.*'}) # ACCEPT_STATE - any more char goes to FAIL_STATE
        STATE_MACHINE.append({ x: {FAIL_STATE} for x in string.ascii_lowercase+'.*'}) # FAIL_STATE - any more char stays in FAIL_STATE
        # print(STATE_MACHINE)
        currentStates = {STARTING_STATE} # NFA have multiple states at any point of time

        # Consume chars from input s one by one
        for c in s:
            nextStates = set()
            for state in currentStates:
                if c in STATE_MACHINE[state]:
                    nextStates |= STATE_MACHINE[state][c]
                if '*' in STATE_MACHINE[state]: # '*' = either gets matched, or skip entirely
                    nextStates |= STATE_MACHINE[state]['*']
            currentStates = nextStates
        if ACCEPT_STATE in currentStates:
            return True

        # Edge case: after all input chars from s are consumed,
        # if we still have remaining patterns not matching any chars,
        # don't quit. They might be optinal characters. For example, patter "a*b*c*" can match empty string
        if len(currentStates) > 0:
            def hasNext(currentStates):
                return set(filter(lambda state: '*' in STATE_MACHINE[state] and state != FAIL_STATE and state != ACCEPT_STATE, currentStates))
            while (candidate_states := hasNext(currentStates)):
                nextStates = set()
                for state in candidate_states:
                    nextStates |= STATE_MACHINE[state]['*']
                if ACCEPT_STATE in nextStates:
                    return True
                currentStates = nextStates

        return ACCEPT_STATE in currentStates
