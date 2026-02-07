package abc443;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

class D2Test {

    private static String stripLastNewline(String s) {
        // 末尾の改行だけを1個除去（\n / \r\n 対応）
        return s.replaceFirst("\\R\\z", "");
    }

    private static String show(String s) {
        // 見比べやすい表示（改行を可視化）
        return s.replace("\r", "\\\\r").replace("\n", "⏎\\n");
    }

    @Test
    void sample1() {
        String input = "5\n5\n5 2 1 3 4\n2\n1 1\n3\n1 3 1\n9\n9 9 8 2 4 4 3 5 3\n20\n7 4 6 2 15 5 17 15 1 8 18 1 5 1 12 11 2 7 8 14";
        String expected = "4\n0\n1\n16\n105";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            D.main(new String[] {});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
                expected,
                result,
                "\n--- DIFF ---\n"
                        + "expected: [" + show(expected) + "]\n"
                        + "result  : [" + show(result) + "]\n");
    }

}
