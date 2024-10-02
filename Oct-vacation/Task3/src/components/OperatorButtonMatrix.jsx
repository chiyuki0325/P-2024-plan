import CalcButton from "./CalcButton.jsx"

export default function OperatorButtonMatrix({ appendExpression, backspace }) {
    return <div className="buttons-column operators">
        <div className="buttons-row">
            {['+', '-', '('].map(char => <CalcButton key={char} char={char} onButtonClick={appendExpression} />)}
        </div>
        <div className="buttons-row">
            {['*', '/', ')'].map(char => <CalcButton key={char} char={char} onButtonClick={appendExpression} />)}
        </div>
        <div className="buttons-row">
            {['^', '='].map(char => <CalcButton key={char} char={char} onButtonClick={appendExpression} />)}
            <CalcButton char="🔙" onButtonClick={backspace} />
        </div>
    </div>
}
