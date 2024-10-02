import CalcButton from "./CalcButton.jsx"

export default function CalcButtonMatrix({ appendExpression }) {
    return <div className="buttons-column buttons-matrix">
        <div className="buttons-row">
            {['1', '2', '3'].map(char => <CalcButton key={char} char={char} onButtonClick={appendExpression} />)}
        </div>
        <div className="buttons-row">
            {['4', '5', '6'].map(char => <CalcButton key={char} char={char} onButtonClick={appendExpression} />)}
        </div>
        <div className="buttons-row">
            {['7', '8', '9'].map(char => <CalcButton key={char} char={char} onButtonClick={appendExpression} />)}
        </div>
        <div className="buttons-row">
            {['0', '.'].map(char => <CalcButton key={char} char={char} onButtonClick={appendExpression} />)}
        </div>
    </div>
}
