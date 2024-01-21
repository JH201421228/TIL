const counter = (state = 0, action: {type: string}) => {
    switch (action.type) {
        case '+':
            return state + 1
        case '-':
            return state - 1
    }
}

export default counter