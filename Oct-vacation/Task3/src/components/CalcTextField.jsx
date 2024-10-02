import {
    Field,
    Textarea
} from '@fluentui/react-components'

export default function CalcTextField({
    value,
    onChange,
    validationState
}) {
    return <>
        <Field 
        label="输入要计算的表达式:"
        validationState={validationState}
        validationMessage={validationState === 'error' ? '表达式格式错误' : ''}
        >
            <Textarea {...{value, onChange}} style={{
                height: '36px',
            }} />
        </Field>
    </>
}