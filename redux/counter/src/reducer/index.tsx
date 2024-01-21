const counter = (state = 0, action: {type: string}) => {
    switch (action.type) {
        case 'INCREMENT':
            return state + 1
        case 'DECEREMENT':
            return state - 1
    }
}

export default counter