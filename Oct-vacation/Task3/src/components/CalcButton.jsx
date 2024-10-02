import {
    Button
} from '@fluentui/react-components'

export default function CalcButton({char, onButtonClick}) {
    return <>
        <Button className='calc-button' onClick={() => onButtonClick(char)}>{char}</Button>
    </>
}