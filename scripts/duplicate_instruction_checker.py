def find_duplicates(input_list: list[str]) -> list[str]:
    seen = set()
    duplicates = set()

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

def create_instruction_list() -> list[str]:
    with open("../nasm-assembler-syntax/syntaxes/nasm.tmLanguage.json", "r") as file:
        lines = file.readlines()

        instruction_groups: list[str] = []
        instructions: list[str] = []

        for index, line in enumerate(lines):
            if "keyword.instructions.group" in line:
                lines[index + 1] = lines[index + 1].replace("\"match\": ", "")
                lines[index + 1] = lines[index + 1].replace("\\\\b", "")
                lines[index + 1] = lines[index + 1].replace("\"(?i:", "")
                lines[index + 1] = lines[index + 1].replace(")\"", "")

                instruction_groups.append(lines[index + 1].strip())

        for instruction_group in instruction_groups:
            instruction_group_list: list[str] = instruction_group.split("|")
            
            for instruction in instruction_group_list:
                instructions.append(instruction)

    return instructions

def main():
    instructions: list[str] = create_instruction_list()
    duplicates: list[str] = find_duplicates(instructions)

    for duplicate in duplicates:
        print(duplicate, end=" ")
    
    print(f"\n\nFound {len(duplicates)} duplicates out of {len(instructions)} instructions")

if __name__ == "__main__":
    main()