export const todos = (state = [], action) => {
    switch (action.type) {
        case 'ADD_TODO':
            return [...state, { id: Date.now(), text: action.text }];
        case 'DELETE_TODO':
            return state.filter((entry) => entry.id !== action.id);
        default:
            return state;
    }
};
